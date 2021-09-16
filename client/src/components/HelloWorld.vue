<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
   <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>


  <b-row>
  <b-col>
  </b-col>
  <b-col>
  <b-form @submit.stop.prevent="onSubmit" v-if="show">
    <b-form-group
      id="input-group-1"
      label="Number Fib:"
      label-for="input-1"
      description="Enter with number to calculate fib"
    >
      <b-form-input
        id="input-1"
        v-model="form.numero"
        type="number"
        placeholder="Enter number"
        required
      ></b-form-input>
    </b-form-group>
    <b-button type="submit" variant="primary">Submit</b-button>
    <b-button @click="getCurrent" variant="danger">Get number</b-button>
    <b-button @click="getAll" variant="danger">Get all</b-button>
  </b-form>
  </b-col>
  <b-col>
  </b-col>
  </b-row>

  {{ this.numbers_cache }}

  {{ this.current }}
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      form: {
        numero: '',
      },
      current: '',
      numbers_cache: [],
      show: true
    }
  },
  methods: {
    onSubmit() {
      this.numbers_cache.push(this.form.numero)
      axios.post('/api/values', {"index": this.form.numero})
        .then(response => { console.log("sucesso", response) })
        .catch(error => console.log("deu erro na /api/values/current", error))
    },
    getCurrent() {
      axios.get('/api/values/current')
        .then(response => { 
          console.log("get current", response) 
        })
        .catch(error => console.log("deu erro na /api/values/current", error))
    },
    getAll() {
      axios.get('/api/values/all')
        .then(response => { 
          console.log("get all", response) 
        })
        .catch(error => console.log("deu erro na /api/values/all", error))
    },

    onReset(event) {
      event.preventDefault()
      // Reset our form values
      this.form.numero = ''
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
