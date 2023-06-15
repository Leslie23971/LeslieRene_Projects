<template #title-header>
  <NuxtLink class="title-anchor" to="/" v-show="displayLangSet == false">Leslie René - Software Engineer</NuxtLink>
  <NuxtLink class="title-anchor" to="/" v-show="displayLangSet == true">Leslie René - Ingénieure Software</NuxtLink>
</template>

<script setup>
 import { ref } from 'vue'
 import { useGlobalStatesStore } from '~/store/globalState'

  const globalSetting = useGlobalStatesStore();

  // const enabled = ref(false); //false = en - true = fr
  const displayLangSet = computed(() => globalSetting.displayLang)
</script>

<style scoped>
@media (max-width: 524px) {
  .title-anchor {
    font-weight: normal;
    font-size: medium;
    white-space:normal;
    color: black;
    background-color: transparent;
  }
  .router-link-exact-active {
    color: black;
  }
}
</style>