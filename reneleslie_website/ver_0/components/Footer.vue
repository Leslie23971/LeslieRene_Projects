<template #copyright-footer>
  <span class="fixed bottom-3" v-show="displayLangSet == false">Designed & Built by Leslie René</span>
  <span class="fixed bottom-3" v-show="displayLangSet == true">Concept & Implémentation par Leslie René</span>
</template>

<script setup>
 import { ref } from 'vue'
 import { useGlobalStatesStore } from '~/store/globalState'

  const globalSetting = useGlobalStatesStore();

  // const enabled = ref(false); //false = en - true = fr
  const displayLangSet = computed(() => globalSetting.displayLang)
</script>

<style scoped>
</style>