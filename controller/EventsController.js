function EventsController(){

    this.getEventJson = (id) => {
        //Create model class that fetches id

        let event = new EventModel();
        let eventJson = null;
        
        eventJson = event.getEventJsonModel(id);

        return eventJson;
    };

    this.setEventJson = (event) => {
        let eventJson = null;

        eventJson = {
            id: event.id,
            name: event.name,
            desc: event.desc,
            donat: event.donat,
            people: event.people
        }
    };

};