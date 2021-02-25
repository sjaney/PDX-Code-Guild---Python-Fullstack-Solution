let app = new Vue({
    el:'#app',
    data:{
        hour: '',
        minute: '',
        second: '',
        meridian: '',
    },
    methods: {
      
    },
    created: function () {
        setInterval(function(){
            [app.hour, app.minute, app.second, app.meridian] = new Date().toLocaleTimeString('en-US').split(/:| /);

        }, 1000);
    }

})