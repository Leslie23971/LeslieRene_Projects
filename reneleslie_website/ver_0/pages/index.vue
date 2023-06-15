<template #default>
  <div class="full-page flex-1 grow">
    <div class="central-block block items-stretch">  
      <!-- false = en - true = fr -->
      <IndexEN v-show="displayLangSet == false"/>
      <IndexFR v-show="displayLangSet == true"/>
    </div>
  </div>
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