import axios from 'axios'

export default class Api {
  constructor() {
    this.client = axios.create()
    this.url = 'http://storage.pythonanywhere.com/'
    this.username = localStorage.username || null
    this.tokenIsValid = false
    this.company_id = localStorage.company_id || null
    this.token = {
      access: localStorage.access || null,
      refresh: localStorage.refresh || null
    }
    //localStorage.removeItem('access')
    //localStorage.removeItem('username')
    if(this.token.access != null){
      this.verify()
    }
    //console.log(this.token)
  }
  registration(reginfo) {
    const formData = new FormData()
    formData.append('first_name', reginfo.firstname)
    formData.append('last_name', reginfo.lastname)
    formData.append('email', reginfo.mail)
    formData.append('phone_number', reginfo.phone)
    formData.append('company_name', reginfo.companyname)
    formData.append('company', JSON.stringify(reginfo.company))
    formData.append('logo', reginfo.logo[0])
    formData.append('city', reginfo.city)
    formData.append('username', reginfo.login)
    formData.append('password', reginfo.password)
    let self  = this
    this.client.post(this.url + 'profile/registration',
      formData,
        {
          headers: {
              'Content-Type': 'multipart/form-data'
          }
        }
    ).then( function(json) {
      console.log(json)
      //self.$router.push('/partners/createadd')

    }).catch(function (error) {
          console.error('UPLOAD FAILURE!', error)
    })
  }
  async login(login, password) {
    const formData = new FormData()
    formData.append('username', login)
    formData.append('password', password)
    let self  = this
    await this.client.post(this.url + 'profile/login',
      formData,
        {
          headers: {
              'Content-Type': 'multipart/form-data'
          }
        }
    ).then( function(response) {
      if(response.status == 200){
        console.log('Прием говна с сервера')
        console.log(response)
        self.token.access = response.data.token
        self.username = response.data.username
        localStorage.username = response.data.username
        localStorage.company_id =
        localStorage.access = response.data.token
        self.tokenIsValid = true
      }

      //self.$router.push('/partners/createadd')

    }).catch(function (error) {
          console.error('UPLOAD FAILURE!', error)
    })
    console.log('конец работы функции')
    return self.token
  }
  async refresh() {
    let self  = this
    const formData = new FormData()
    formData.append('refresh', localStorage.getItem('refresh'))
    await this.client.post(this.url + 'profile/token/refresh',
      formData,
        {
          headers: {
              'Content-Type': 'multipart/form-data',
              'Authorization': 'Bearer ' + localStorage.getItem('access')
          }
        }
    ).then( function(response) {
      if(response.status == 200){
        console.log('Обновляем токен')
        console.log(response)
        self.token.access = response.data.access
        localStorage.access = response.data.access
        self.token.refresh = response.data.refresh
        localStorage.refresh = response.data.refresh
      }

      //self.$router.push('/partners/createadd')

    }).catch(function (error) {
      localStorage.removeItem('access')
      console.error('UPLOAD FAILURE!', error)
    })
    console.log('конец работы функции')
    return self.token
  }
  async verify() {
    let self  = this
    const formData = new FormData()
    formData.append('token', self.token.access)
    await this.client.post(this.url + 'profile/token/verify',
        formData,
        {
          headers: {
              'Content-Type': 'multipart/form-data',
              'Authorization': 'Bearer ' + localStorage.getItem('access')
          }
        }
    ).then( function(response) {
      if(response.status == 200){
        console.log('Токен валиден')
        self.tokenIsValid = true
        /*console.log(response)
        self.token.access = response.data.access
        localStorage.access = response.data.access
        self.token.refresh = response.data.refresh
        localStorage.refresh = response.data.refresh*/
      }else {
        console.log('Неверный токен')
        self.tokenIsValid = false
      }

      //self.$router.push('/partners/createadd')

    }).catch(function (error) {
          console.error('UPLOAD FAILURE!', error)
          console.log(error.response)
          if(error.response.status === 401 && self.token.refresh != null) {
            console.log('GOVNO TOKEN')
            self.refresh().then(
              function(response) {
                self.verify()
              }
            )
          }
          if(error.response.status === 400) {
            self.tokenIsValid = false
            console.log('Нужно авторизироваться')
            localStorage.removeItem('access')
            localStorage.removeItem('username')
          }
    })
  }
  async logout() {
    let self  = this
    self.token.access = null
    localStorage.removeItem('access')
    self.token.refresh = null
    localStorage.removeItem('refresh')
    localStorage.removeItem('username')
    console.log(self.token)
    console.log(localStorage.access)
    await this.client.post(this.url + 'profile/logout',
      {},
        {
          headers: {
              'Content-Type': 'multipart/form-data',
              'Authorization': 'Bearer ' + localStorage.getItem('access')
          }
        }
    ).then( function(response) {
      self.token.access = null
      localStorage.removeItem('access')
      self.token.refresh = null
      localStorage.removeItem('refresh')

    }).catch(function (error) {
          console.error('UPLOAD FAILURE!', error)
    })
    console.log('конец работы функции')
    return 1
  }
  async getUser() {
    let self  = this
    console.log('ИМЯ' + self.username)
    await this.client.get(this.url + 'profile/get/' + self.username,
        {
          headers: {
              'Content-Type': 'multipart/form-data',
              'Authorization': 'Bearer ' + localStorage.getItem('access')
          }
        }
    ).then( function(response) {
      self.response = response
      self.company_id = response.data.companies[0].id
      localStorage.company_id = response.data.companies[0].id
      console.log(response)

    }).catch(function (error) {
          console.error('UPLOAD FAILURE2!', error)
          console.log(error.response.status)
          if(error.response.status === 401) {
            console.log('REFRESH TOKEN')
            self.refresh().then(
              function(response) {
                self.getUser()
              }
            )
          }
    })
    console.log('конец работы функции')
    return self.response
  }
  async getCompany(id) {
    let self  = this
    await this.client.get(this.url + 'company/' + id,
        {
          headers: {
              'Content-Type': 'multipart/form-data',
                'Authorization': 'Bearer ' + localStorage.getItem('access')
          }
        }
    ).then( function(response) {
      console.log('Данные компании')
      self.response = response
      console.log(response)

    }).catch(function (error) {
          console.error('UPLOAD FAILURE2!', error)
    })
    console.log('конец работы функции')
    return self.response
  }
  async postStorage(reginfo) {
    let self  = this
    const formData = new FormData()
    formData.append('address', reginfo.address)
    formData.append('company_id', self.company_id)
    formData.append('company_owner', self.username)
    formData.append('square', reginfo.square)
    formData.append('price', reginfo.price)
    formData.append('description', reginfo.description)
    //formData.append('images', reginfo.images)
    for( var i = 0; i < reginfo.images.length; i++ ){
      let file = reginfo.images[i];
      formData.append('image' + i, file);
    }
    formData.append('description', reginfo.description)
    await this.client.post(this.url + 'storage/',
      formData,
        {
          headers: {
              'Content-Type': 'multipart/form-data',
              'Authorization': 'Bearer ' + localStorage.getItem('access')
          }
        }
    ).then( function(response) {
      console.log(response)
      //self.$router.push('/partners/createadd')

    }).catch(function (error) {
          console.error('UPLOAD FAILURE!', error)
    })
  }
  async getAllStorages() {
    let self  = this
    await this.client.get(this.url + 'company/' + self.company_id + '/storages',
        {
          headers: {
              'Content-Type': 'multipart/form-data',
              'Authorization': 'Bearer ' + localStorage.getItem('access')
          }
        }
    ).then( function(response) {
      self.response = response.data
      console.log('Мои объявления')
      console.log(response)
    }).catch(function (error) {
          console.error('UPLOAD FAILURE!', error)
    })
    console.log('конец работы функции')
    return self.response
  }
  async getImg(path) {
    console.log(path)
    let self  = this
    await this.client.get(this.url + path,
        {
          headers: {
              'Content-Type': 'image/png',
              'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

          }
        }
    ).then( function(response) {
      self.response = response.data
      console.log('Мои объявления')
      console.log(response)
    }).catch(function (error) {
          console.error('UPLOAD FAILURE!', error)
    })
    console.log('конец работы функции')
    return self.response
  }

}
