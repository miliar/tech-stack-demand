import requests
from config import KEYWORDS_API


class JobKeywordsParser:
    def __init__(self, text):
        self.text = text

    def get(self):
        keywords = ' '.join(requests.get(KEYWORDS_API +
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
                          'this', 'build', 'performance', 'frameworks',
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
                          'count', 'plugins', 'repository', 'copy', 'new-operator', 'product',
                          'at-command', 'environment', 'system', 'project', 'jobs', 'roles',
                          'communication', 'using', 'apply', 'member', 'free', 'standards',
                          'where-clause', 'core', 'profile', 'send', 'shapes',
                          'next', 'global', 'implementation', 'share', 'external', 'contact',
                          'production', 'unique', 'area', 'between', 'design-patterns',
                          'live', 'public', 'orientation', 'each', 'space', 'documentation',
                          'equals', 'access', 'document', 'enterprise', 'expect', 'status',
                          'native', 'base', 'record', 'playback', 'relationship', 'identity',
                          'cycle', 'execution', 'clear', 'state', 'account', 'specifications',
                          'resources', 'back', 'lifecycle', 'connect', 'addition', 'point',
                          'local', 'main', 'put', 'responsive', 'action', 'workflow', 'libraries',
                          'long-integer', 'target', 'execute', 'require', 'translate', 'handle',
                          'settings', 'launch', 'release', 'comparable', 'difference', 'protected',
                          'transparent', 'expand', 'options', 'push', 'hierarchy', 'transform',
                          'private', 'move', 'line', 'transparency', 'extends', 'metrics',
                          'refactoring', 'module', 'show', 'protocols', 'validation', 'driver',
                          'virtual', 'add', 'center', 'blogs', 'combinations', 'shared', 'progress',
                          'definition', 'call', 'message', 'scheme', 'break', 'selection', 'updates',
                          'procedure', 'constants', 'submit', 'history', 'option', 'reduce', 'payment',
                          'schedule', 'visibility', 'collections', 'save', 'layer',
                          'limit', 'parent', 'self', 'display', 'join', 'super', 'optional']
        return ' '.join([k for k in keywords.split() if k not in false_positive])
