<template>
  <div class="columns">
    <div class="content">
      <div class="column">
        <h1>Listagem de Pessoas</h1>
        <div class="content">
          <div class="is-horizontal">
            <div class="field-body">
              <div class="field">
                <p class="control">
                  <input class="input is-primary" v-model="search" />
                </p>
              </div>
            </div>
            <br />
            <button class="button is-info" @click.prevent="get_search">Pesquisar</button>
          </div>
        </div>
        <table class="table">
          <thead>
            <tr>
              <td>ID</td>
              <td>Nome</td>
              <td>Data da Admissão</td>
              <td colspan="2">Opções</td>
            </tr>
          </thead>
          <tbody>
            <tr v-for="person in persons" v-bind:key="person.id_pessoa">
              <td>{{ person.id_pessoa }}</td>
              <td>{{ person.nome.split(' ')[0] }}</td>
              <td>{{ getTime(person.data_admissao) }}</td>
              <td><a @click.prevent="updatePerson(person)" href="">Editar</a> |
                <a @click.prevent="deletePerson(person)">Deletar</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="column">
      <div class="content">
      <h1 v-if="id_pessoa == 0">Cadastrar Pessoa</h1>
      <h1 v-else>Alterar Pessoa</h1>
      <div class="is-horizontal">
        <div class="is-normal">
          <label class="label">ID</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control">
              <input class="input is-primary" v-model="id_pessoa" />
            </p>
          </div>
        </div>
      </div>
      <div class="is-horizontal">
        <div class="is-normal">
          <label class="label">Nome</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control">
              <input class="input is-primary" v-model="nome" />
            </p>
          </div>
        </div>
      </div>
      <div class="is-horizontal">
        <div class="is-normal">
          <label class="label">CPF</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control">
              <input class="input is-primary" v-model="cpf" />
            </p>
          </div>
        </div>
      </div>
      <div class="is-horizontal">
        <div class="is-normal">
          <label class="label">RG</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control">
              <input class="input is-primary" v-model="rg" />
            </p>
          </div>
        </div>
      </div>
      <div class="is-horizontal">
        <div class="is-normal">
          <label class="label">Data de Nascimento</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control">
              <input type="text" class="input is-primary" v-model="data_nascimento" />
            </p>
          </div>
        </div>
      </div>
      <div class="is-horizontal">
        <div class="is-normal">
          <label class="label">Data de Admissão</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control">
              <input type="text" class="input is-primary" v-model="data_admissao" />
            </p>
          </div>
        </div>
      </div>
      <div class="is-horizontal">
        <div class="is-normal">
          <label class="label">Função</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control">
              <input class="input is-primary" v-model="funcao" />
            </p>
          </div>
        </div>
      </div>
      <br>
        <div class="field is-grouped">
          <div class="control">
            <button class="button is-link" @click.prevent="savePerson">Confirmar</button>
          </div>
          <div class="control">
            <button class="button" @click.prevent="resetPerson">Limpar</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      persons: [],
      id_pessoa: 0,
      nome: '',
      cpf: '',
      rg: '',
      data_nascimento: '',
      data_admissao: '',
      funcao: '',
      search: ''
    }
  },
  methods: {
    async allPersons() {
      const res = await fetch('http://127.0.0.1:5000/');
      const data = await res.json();
      this.persons = data;
    },
    async savePerson() {
      const base_url = 'http://127.0.0.1:5000/'
      let url = ''
      const id_pessoa = this.id_pessoa
      const nome = this.nome
      const cpf = this.cpf
      const rg = this.rg
      const data_nascimento = this.data_nascimento
      const data_admissao = this.data_admissao
      const funcao = this.funcao
      let data = {
        nome: nome,
        cpf: cpf,
        rg: rg,
        data_nascimento: data_nascimento,
        data_admissao: data_admissao,
        funcao: funcao
      }
      if (id_pessoa === 0) {
        console.log("Inserir")
        url = base_url + 'adicionar'
      } else {
        console.log("Atualizar")
        url = base_url + 'atualizar'
        data = Object.assign(data, { id_pessoa: id_pessoa})
      }
      console.log(data, url)
      const config = {
         headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}
      }
      fetch( url, {
          method: 'POST',
          body: JSON.stringify( data ),
          headers: config
      } )
      .then((data) => {
          console.log('Success:', data);
          this.resetPerson()
          this.allPersons()
      })
      .catch((error) => {
          console.error('Error:', error);
      })
    },
    async updatePerson(pessoa) {
      this.id_pessoa = pessoa.id_pessoa
      this.nome = pessoa.nome
      this.cpf = pessoa.cpf
      this.rg = pessoa.rg
      this.data_nascimento = this.getTime(pessoa.data_nascimento)
      this.data_admissao = this.getTime(pessoa.data_admissao)
      this.funcao = pessoa.funcao
    },
    resetPerson() {
      this.id_pessoa = 0
      this.nome = ""
      this.cpf = ""
      this.rg = ""
      this.data_nascimento = ""
      this.data_admissao = ""
      this.funcao = ""
    },
    async deletePerson(pessoa) {
       if(confirm("Você realmente quer apagar o registro?")) {
         const base_url = 'http://127.0.0.1:5000/'
         let data = {
           id_pessoa: pessoa.id_pessoa
         }
         await fetch(base_url + 'deletar', {
           method: "DELETE",
           body: JSON.stringify(data),
         })
         .then((data) => {
           console.log('Success:', data.status);
           this.allPersons()
         })
         .catch((error) => {
           console.error('Error:', error);
         })
       }
      },
    async get_search () {
      const base_url = 'http://127.0.0.1:5000/'
      let nome = this.search
      const res = await fetch(base_url + nome)
      const data = await res.json();
      this.persons = data;
      this.search = ''
    },
    getTime(location) {
      return new Date(location).toLocaleDateString()
    }
  },
  mounted() {
    this.allPersons()
  }
}
</script>
