<template>
  <div>
    <h1>{{ titulo }}</h1>
    <div class="container is-fluid">
      <div class="columns">
        <a class="button is-info" href="./AddPessoa.vue">Adicionar Pessoas</a>
      </div>
      <div class="table-container">
        <table class="table is-bordered is-striped">
          <thead>
            <tr>
              <td>ID</td>
              <td>Nome</td>
              <td>Data da Admissão</td>
              <td colspan="2">Opções</td>
            </tr>
          </thead>
          <tbody v-for="pessoa in pessoas" v-bind:key="pessoa.id_pessoa">
            <tr>
              <td>{{ pessoa.id_pessoa }}</td>
              <td class="text-left">{{ pessoa.nome }}</td>
              <td>{{ pessoa.data_admissao }}</td>
              <td>
                <a href="">Alterar</a> |
                <a href="">Deletar</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <nav class="pagination is-centered" role="navigation" aria-label="pagination">
        <a class="pagination-previous">Previous</a>
        <a class="pagination-next">Next page</a>
        <ul class="pagination-list">
          <li><a class="pagination-link" aria-label="Goto page 1">1</a></li>
          <li><span class="pagination-ellipsis">&hellip;</span></li>
          <li><a class="pagination-link" aria-label="Goto page 45">45</a></li>
          <li><a class="pagination-link is-current" aria-label="Page 46" aria-current="page">46</a></li>
          <li><a class="pagination-link" aria-label="Goto page 47">47</a></li>
          <li><span class="pagination-ellipsis">&hellip;</span></li>
          <li><a class="pagination-link" aria-label="Goto page 86">86</a></li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Lista-de-Pessoas',
  data () {
      return {
          titulo: "Lista de Pessoas",
          pessoas: {}
      }
  },
  columns: ['nome', 'rg', 'cpf', 'data_nascimento', 'data_admissao', 'funcao'],
  methods: {
    async getPessoas() {
      const res = await fetch('http://127.0.0.1:5000/');
      const data = await res.json();
      this.pessoas = data;
    }
  },
  mounted() {
    this.getPessoas()
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
