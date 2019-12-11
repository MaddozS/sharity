function EventCRUD(){

    this.getEventsDB = async () => {

        try{
            const response = await fetch('https://jsonplaceholder.typicode.com/comments?postId=1');
            const json = await response.json();

            return json;
                
        }catch(error){
            console.log(error);
        }
    }

    this.getSingleEvent = async (id) => {
        try{
            const response = await fetch('https://jsonplaceholder.typicode.com/posts/' + id);
            const json = await response.json();

            return json;
                
        }catch(error){
            console.log(error);
        }
    }

    this.postEventDB = async (elemJson) => {
        try{
            const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
                                    method: 'POST',
                                    body: elemJson,
                                    headers: {
                                    "Content-type": "application/json; charset=UTF-8"
                                    }
                                });

            const json = await response.json();

            console.log(json);

            console.log(response);
            
        }catch(e){
            console.log(e);
        }
    }

}