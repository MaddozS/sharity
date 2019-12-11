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

    this.searchEvent = async (event) => {
        let band = false;
        let events = await this.getEvents();

        console.log(events);

        if(this.validateDonat(event)){
            for(let i = 0; i < events.length; i++){
                if(event == events[i].name){
                    band = true;
                }
            }
        }else{
            alert('Missed input field');
        }

        if(band){
            window.location.href = "event.html";
        }else{
            alert('Event not found');
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

    this.validateDonat = (val) => {
        let band = true;

        if(val == ''){
            band = false;
        }

        return band;

    }

    this.createEvent = async () => {
        let conn = new EventCRUD();
        conn.postEventDB(eventJson);
    }


    this.getEvents = async () => {

        let elem;

        let conn = new EventCRUD();
        elem = await conn.getEventsDB();

        return elem;
    }

    this.dynamicEve = (info, json) => {

        let template = Handlebars.compile(info);

        let quoteData = template({
            json
        })
        document.getElementById("cards").innerHTML += quoteData;
    }

    this.dynamicEvent = async (info1, info2, info3, info4) => {
        let template1 = Handlebars.compile(info1);
        let template2 = Handlebars.compile(info2);
        let template3 = Handlebars.compile(info3);
        let template4 = Handlebars.compile(info4);

        let jsonData;


        let event = new EventCRUD();

        jsonData = await event.getSingleEvent(2);

        console.log(jsonData);

        let quoteData1 = template1({
            name: jsonData.title
        });

        let quoteData2 = template2({
            des:jsonData.body
        });

        let quoteData3 = template3({
            donation: jsonData.id
        });

        let quoteData4 = template4({
            people: jsonData.userId
        });


        console.log(quoteData3);

        document.getElementById('evName').innerHTML += quoteData1;
        document.getElementById('evDes').innerHTML += quoteData2;
        document.getElementById('evDonat').innerHTML += quoteData3;
        document.getElementById('evPeople').innerHTML += quoteData4;
    }

    this.dynamicDes = async (data) => {
        let template = Handlebars.compile(data);

        let jsonData;

        let event = new EventCRUD();

        jsonData = await event.getSingleEvent(1);

        console.log(jsonData);

        let quoteData = template({
            des: jsonData.body
        });

        document.getElementById('evDes').innerHTML += quoteData;
    }


};