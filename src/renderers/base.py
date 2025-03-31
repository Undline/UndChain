from typing import Any, Dict, List

class BaseRenderer:
    
    def setup(self):
        '''
        Called once before rendering. Good place for engine initialization.
        '''

        pass

    def render_widget_tree(self, widget_tree: List[Dict[str, Any]]) -> None:
        '''
        Where we actually traverse and draw the widgets.
        '''

        raise NotImplementedError

    def teardown(self):
        '''
        Called at shutdown to release resources, close windows, etc.
        '''

        pass

    def update(self, dt: float):
        '''
        (Optional) For real-time or game-like engines that need a per-frame update.
        '''

        pass

    def on_intent(self, intent_name: str, widget_info: Dict[str, Any]) -> None:
        '''
        This method is called when a widget is interacted with.
        E.g. 'on_click' triggers 'scroll_to_top', etc.
        '''

        pass

    def update_widget(self, widget_info: Dict[str, Any]) -> None:
        '''
        Called when a single widget's data changes and we want
        to re-draw or adjust only that widget (and possibly children).
        '''
        
        raise NotImplementedError
