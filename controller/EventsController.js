function EventsController(){

    let obj = {};
    let eventJson;

    this.setEventJson = (reg) => {

        if(this.validateForm(reg)){
            for(let i = 0 ; i < reg.length - 1; i++){
                let item = reg.item(i);
                obj[item.name] = item.value;
            }
    
            eventJson = JSON.stringify(obj);
            console.log(eventJson);
        }else{
            alert('Missed input field');
        }
    }

    this.validateForm = (val) => {
        let band = true;

        for(let i = 0 ; i < val.length - 1; i++){
            let item = val.item(i);
            if(item.value == ''){
                band = false;
            }
        }

        return band;
    }

    this.searchEvent = (event) => {
        console.log('found ' + event);
    }

    this.getEvents = async () => {

        let elem;

        let conn = new EventCRUD();
        elem = await conn.getEventsDB();

        return elem;
    }

    this.dynamicEve = (info, json) => {
        let quoteInfo = document.getElementById('quote-template').innerHTML;
    
        let template = Handlebars.compile(quoteInfo);
    
        let data = {}
        
        json.forEach(elem => {
          data.name = elem.name;
          data.body = elem.body;
        });
    
        console.log(data);
    
        console.log(json);
    
        let quoteData = template({
          json
        })
        document.getElementById("cards").innerHTML += quoteData;
      }

};