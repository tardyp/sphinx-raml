from docutils.parsers.rst import Directive
import pkg_resources
from docutils import nodes
import ramlfications
import os

class raml(nodes.Element):
    pass


class RamlDirective(Directive):

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}

    def run(self):
        node = raml()
        node.document = self.state.document
        basepath  = os.path.dirname(self.state.document.current_source)
        parsed = ramlfications.load(os.path.join(basepath, self.arguments[0]))
        node['expr'] = parsed
        self.state.nested_parse(self.content, self.content_offset,
                                node, match_titles=1)
        return [node]


def html_visit_raml(self, node):
    self.body.append("okok" + repr(node['expr']))


def html_end_raml(self, node):
    pass

def setup(app):
    app.add_node(raml, html=(html_visit_raml, html_end_raml))
    app.add_directive('raml', RamlDirective)

    return {
        'version': pkg_resources.require('ramlfications')[0].version
    }
