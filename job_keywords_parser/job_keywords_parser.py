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
        false_positive = ['for-loop', 'testing', 'web', 'service', 'process', 'commit',
                          'this', 'build', 'performance', 'frameworks', 'operators',
                          'if-statement', 'makefile', 'architecture', 'task', 'time',
                          'get', 'stack', 'shared-libraries', 'focus', 'field', 'hidden',
                          'dynamic', 'position', 'optimization', 'key', 'while-loop',
                          'find', 'include', 'set', 'client', 'interface', 'http', 'offline',
                          'computer-vision', 'background', 'components', 'location', 'date',
                          'directory', 'methods', 'coffeescript', 'controls', 'types',
                          'range', 'hyperlink', 'package', 'class', 'structure', 'signals',
                          'version', 'report', 'session', 'email', 'search', 'extend',
                          'numbers', 'path', 'image', 'forms', 'colors', 'https', 'solver',
                          'object', 'view', 'scope', 'reference', 'try-catch', 'rules',
                          'installation', 'configuration', 'function', 'coordinates', 'input',
                          'tags', 'math', 'command', 'connection', 'alignment', 'material',
                          'modul', 'list', 'iteration', 'logic', 'express', 'reporting',
                          'load', 'prepared-statement', 'conditional-statements', 'dependencies',
                          'max', 'layout', 'loops', 'text', 'size', 'future', 'final',
                          'click', 'certificate', 'request', 'map', 'button', 'migration',
                          'file', 'case', 'match', 'chef', 'format', 'upload', 'sharing',
                          'character', 'post', 'expression', 'static', 'select', 'criteria',
                          'count', 'plugins', 'repository', 'copy', 'new-operator', 'product',
                          'at-command', 'environment', 'system', 'project', 'jobs', 'roles',
                          'communication', 'using', 'apply', 'member', 'free', 'standards',
                          'where-clause', 'core', 'profile', 'send', 'shapes', 'agile',
                          'next', 'global', 'implementation', 'share', 'external', 'contact',
                          'production', 'unique', 'area', 'between', 'design-patterns', 'views',
                          'live', 'public', 'orientation', 'each', 'space', 'documentation',
                          'equals', 'access', 'document', 'enterprise', 'expect', 'status',
                          'native', 'base', 'record', 'playback', 'relationship', 'identity',
                          'cycle', 'execution', 'clear', 'state', 'account', 'specifications',
                          'resources', 'back', 'lifecycle', 'connect', 'addition', 'point',
                          'local', 'main', 'put', 'responsive', 'action', 'workflow', 'libraries',
                          'long-integer', 'target', 'execute', 'require', 'translate', 'handle',
                          'settings', 'launch', 'release', 'comparable', 'difference', 'protected',
                          'transparent', 'expand', 'options', 'push', 'hierarchy', 'transform',
                          'private', 'move', 'line', 'transparency', 'extends', 'metrics', 'sample',
                          'refactoring', 'module', 'show', 'protocols', 'validation', 'driver',
                          'virtual', 'add', 'center', 'blogs', 'combinations', 'shared', 'progress',
                          'definition', 'call', 'message', 'scheme', 'break', 'selection', 'updates',
                          'procedure', 'constants', 'submit', 'history', 'option', 'reduce', 'payment',
                          'schedule', 'visibility', 'collections', 'save', 'layer', 'd', 'channel',
                          'limit', 'parent', 'self', 'display', 'join', 'super', 'optional', 'branch',
                          'lines', 'capture', 'average', 'output', 'draw', 'publish', 'watch', 'configure',
                          'children', 'upgrade', 'screen', 'wait', 'bit', 'abstract', 'dialog', 'constraints',
                          'split', 'edit', 'associations', 'figure', 'contacts', 'arm', 'response', 'mean', 'exists']
        return ' '.join([k for k in keywords.split() if k not in false_positive])
