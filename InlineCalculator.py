import sublime, sublime_plugin, re

class InlineCalculatorCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    selected_regions = self.view.sel()
    for region in selected_regions:
      expr = self.view.substr( region );
      if re.match('^[0-9+\-*/%\(\). ]+$', expr):
        result = eval( expr )
        print result
        self.view.replace( edit, region, str( result ) )
