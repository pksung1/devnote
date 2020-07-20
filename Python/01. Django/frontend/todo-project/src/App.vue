<template>
  <div id="app">
    <Header />
    <Content>
      <router-view/>
    </Content>
  </div>
</template>

<script>
import Header from './components/layout/Header';
import Content from './components/layout/Content';

export default {
  name: 'App',
  components: {
    Header,
    Content,
  },
};
</script>

<style lang="scss">
@import 'node_modules/bootstrap/scss/bootstrap';
@import 'node_modules/bootstrap-vue/src/index.scss';
</style>
