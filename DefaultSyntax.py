import sublime, sublime_plugin

class DefaultSyntax(sublime_plugin.EventListener):
    def on_new(self, view):
        # setting = view.settings().get('default_syntax', 'Packages/Text/Plain text.tmLanguage')
        setting = view.settings().get('default_syntax', 'Packages/Miva IDE/MVT.tmLanguage')
        setting = sublime.active_window().active_view().settings().get('default_syntax', setting)
        view.set_syntax_file(setting)
