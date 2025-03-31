class BaseRenderer:
    '''
    Abstract base class for all renderers.
    '''

    def render_widget_tree(self, widget_tree):
        raise NotImplementedError("Must implement render_widget_tree.")
