class EventsManager:

    __listeners = {}

    def attach_listener(self, event_type, listener):
        if event_type not in self.__listeners:
            self.__listeners.setdefault(event_type, [])
        self.__listeners[event_type].append(listener)

    def detach_listener(self, event_type, listener):
        self.__listeners[event_type].remove(listener)

    def notify_listeners(self, event_type, data):
        for listener in self.__listeners[event_type]:
            listener.update(data)


class EventListener:

    @staticmethod
    def update(data):
        pass


