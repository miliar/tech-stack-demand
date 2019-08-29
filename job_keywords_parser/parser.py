from helper import get_consumer, get_producer
import requests


class JobKeywordsParser:
    def __init__(self, text):
        self.text = text

    def get(self):
        keywords = ' '.join(requests.get('http://keywords_api:4000/keywords/' +
                                         self._preprocess_text()).json())
        return self._exclude_false_positive(keywords)

    def _preprocess_text(self):
        text = ''.join(
            ' ' if c in '! ” $ % & ( ) * / : ; , < = > ? @ | [ ] ` ~ ^ { } \\ \''.split() else c for c in self.text)
        text = text.replace('. ', ' ').replace(
            '.\n', ' ').replace('#', 'sharp')
        return ' '.join(text.lower().split())

    def _exclude_false_positive(self, keywords):
        false_positive = ['for-loop', 'testing', 'web', 'service', 'process',
                          'this', 'build', 'performance', 'frameworks', 'join',
                          'if-statement', 'makefile', 'architecture', 'task', 'time',
                          'get', 'stack', 'shared-libraries', 'focus', 'field',
                          'dynamic', 'position', 'optimization', 'key', 'while-loop',
                          'find', 'include', 'set', 'client', 'interface',
                          'computer-vision', 'background', 'components', 'location', 'date',
                          'directory', 'methods', 'coffeescript', 'controls', 'types',
                          'range', 'hyperlink', 'package', 'class', 'structure',
                          'version', 'report', 'session', 'email', 'search',
                          'numbers', 'path', 'image', 'forms', 'colors',
                          'object', 'view', 'scope', 'reference', 'try-catch',
                          'installation', 'configuration', 'function', 'coordinates', 'input',
                          'tags', 'math', 'command', 'connection', 'alignment',
                          'modul', 'list', 'iteration', 'logic', 'express',
                          'load', 'prepared-statement', 'conditional-statements', 'dependencies',
                          'max', 'layout', 'loops', 'text', 'size',
                          'click', 'certificate', 'request', 'map', 'button', 'migration',
                          'file', 'case', 'match', 'chef', 'format', 'upload',
                          'character', 'post', 'expression', 'static', 'select',
                          'count', 'plugins', 'repository', 'copy']
        return ' '.join([k for k in keywords.split() if k not in false_positive])


if __name__ == '__main__':
    consumer = get_consumer('job_descriptions')
    producer = get_producer()

    for description in consumer:
        job_keywords = JobKeywordsParser(description.value).get()
        producer.send('job_keywords',
                      value=job_keywords,
                      key=description.key)
        print('SEND KEY: ' + description.key)
        print('SEND VALUE: ' + job_keywords, flush=True)
