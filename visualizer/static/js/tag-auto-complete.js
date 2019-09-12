var main = new autoComplete({
    selector: '#search',
    minChars: 1,

    source: function (term, suggest) {
        var query = "match (x) WHERE toLower(x.name) contains $term return DISTINCT x.name AS name, labels(x) as label order by name LIMIT 20";
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
        var label = item[1];
        var imagePath = popoto.provider.node.getImagePath({
            label: label,
            type: popoto.graph.node.NodeTypes.VALUE,
            attributes: {name: name}
        });

        

        return '<div class="autocomplete-suggestion" data-id="' + name + '" data-rel="USES" data-label="' + label + '" data-search="' + search + '"><img width="20px" height="20px" src="' + imagePath + '"> ' + label + ": "+ name.replace(re, "<b>$1</b>") + '</div>';
    },
    onSelect: function (e, term, item) {
        var id = item.getAttribute('data-id');
        var rel = item.getAttribute('data-rel');
        var label = item.getAttribute('data-label');
        var searchInput = document.getElementById('search');

        if (label === 'Tag'){
            popoto.graph.node.addRelatedValues(popoto.graph.getRootNode(), [{
                id: id,
                rel: rel,
                label: label
            }]);
        }
        else {
            popoto.graph.mainLabel = {
                label: label,
                value: {
                    name: id
                },
                rel: [
                {
                    label: "USES",
                    target: {
                        label: "Tag"
                    }
                }
                ]
            };
            popoto.tools.reset();
            popoto.graph.mainLabel = "Company";
        }

        searchInput.value = '';
        searchInput.blur();
    }
});