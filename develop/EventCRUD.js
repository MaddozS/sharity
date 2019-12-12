function EventCRUD(){

    this.getEventsDB = async () => {

        try{
            const response = await fetch('http://ec2-3-92-65-138.compute-1.amazonaws.com:5000/api/events/');
            const json = await response.json();

            return json;
                
        }catch(error){
            console.log(error);
        }
    }

    this.getSingleEvent = async (id) => {
        try{
            const response = await fetch('http://ec2-3-92-65-138.compute-1.amazonaws.com:5000/api/events/' + id);
            const json = await response.json();

            return json;
                
        }catch(error){
            console.log(error);
        }
    }

    this.postEventDB = async (elemJson) => {

        let band = false;

        try{
            const response = await fetch('http://ec2-3-92-65-138.compute-1.amazonaws.com:5000/api/events/', {
                                    method: 'POST',
                                    body: elemJson,
                                    headers: {
                                    "Content-type": "application/json; charset=UTF-8"
                                    }
                                });

            const json = await response.json();

            band = true;

            console.log(json);

            console.log(response);
            
        }catch(e){
            console.log(e);
        }

        return band;
    }

}