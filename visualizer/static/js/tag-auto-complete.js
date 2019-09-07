var main = new autoComplete({
    selector: '#search',
    minChars: 0,

    source: function (term, suggest) {
        var query = "match (c:Company)-[r]->(t:Tag) WHERE (toLower(t.name) contains $term) return DISTINCT t.name AS name, type(r) as rel, count(t) as occurence order by occurence desc LIMIT 20";

        var statements = [
            {
                "statement": query,
                "parameters": {
                    term: term.toLowerCase()
                },
                "resultDataContents": ["row"]
            }
        ];

        popoto.logger.info("AutoComplete ==> ");
        popoto.rest.post(
            {
                "statements": statements
            })
            .done(function (data) {
                var res = data.results[0].data.map(function (d) {
                    return d.row
                });
                suggest(res);
            })
            .fail(function (xhr, textStatus, errorThrown) {
                console.error(xhr, textStatus, errorThrown);
                suggest([]);
            });
    },
    renderItem: function (item, search) {
        search = search.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&amp;');
        var re = new RegExp("(" + search.split(' ').join('|') + ")", "gi");
        var name = item[0];
        var rel = item[1];
        var label = "Tag";
        

        return '<div class="autocomplete-suggestion" data-id="' + name + '" data-rel="' + rel + '" data-label="' + label + '" data-search="' + search + '"> ' + rel + " "+ name.replace(re, "<b>$1</b>") + '</div>';
    },
    onSelect: function (e, term, item) {
        var id = item.getAttribute('data-id');
        var rel = item.getAttribute('data-rel');
        var label = item.getAttribute('data-label');

        document.getElementById('search').value = "";
        $("#search").blur();

        popoto.graph.node.addRelatedValues(popoto.graph.getRootNode(), [{
            id: id,
            rel: rel,
            label: label
        }]);

    }
});