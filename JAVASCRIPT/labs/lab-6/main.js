let app = new Vue({
    el: '#app',
    data: {
        imgUrl: '',
        category: [],
        catCategory: ''
    },
    methods: {
        submit: async function() {
            let response = await axios({
                method: 'get',
                url: 'https://api.thecatapi.com/v1/images/search',
                params: {
                    category_ids: this.catCategory
                }
            })
          
            this.imgUrl = response.data[0].url
        }
    },

    created: async function() {
        let response = await axios({
            method:'get',
            url: 'https://api.thecatapi.com/v1/categories'
        })
        this.category = response.data
    }
})