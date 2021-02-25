let app = new Vue ({
    el: "#app",
    data: {
        lat: '',
        lon: '',
        date: '',
        time: '',
        temp:'',
        icon: '',
        iconUrl: '',
        icons: [],
        unix_timestamp: '',
    },
    created: function() {
        navigator.geolocation.getCurrentPosition(position =>{
            this.lat = position.coords.latitude.toFixed(6);
            this.lon = position.coords.longitude.toFixed(6);
        },
        )

    },

    watch: {
        lon: async function() {
            response = await axios({
                method:'get',
                url: 'https://api.openweathermap.org/data/2.5/onecall?',
                params: {
                    appid: apiKey,
                    lat: this.lat,
                    lon: this.lon,
                    units: 'imperial',
                }
            })
           
            this.time = new Date(response.data.current.dt * 1000).toLocaleTimeString()
            this.date = new Date(response.data.current.dt * 1000).toLocaleDateString()
            this.temp = response.data.current.temp
            this.icon = response.data.current.weather[0].icon
            this.iconUrl = 'http://openweathermap.org/img/wn/' + this.icon + '.png'
            
            console.log(response.data)
            
        }
    }



})