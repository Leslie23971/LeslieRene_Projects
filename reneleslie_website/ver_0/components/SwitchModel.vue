<template>
  <SwitchGroup>
    <div class="switch-div flex items-center">
      <SwitchLabel class="mr-2">en</SwitchLabel>
      <Switch
        v-model="enabled"
        :class="enabled ? 'bg-black-900' : 'bg-black-700'"
        class="relative inline-flex h-6 w-11 items-center rounded-full transition-colors outline outline-offset-2 outline-white-500"
      >
        <span
          :class='enabled ? "translate-x-6" : "translate-x-1"'
          class="inline-block h-6 w-6 transform rounded-full bg-white transition-transform max-[524px]:bg-black"
        />
      </Switch>
      <SwitchLabel class="ml-2">fr</SwitchLabel>
    </div>
  </SwitchGroup>

  <!-- <p>from SwitchModel : enabled =  {{ enabled }}</p> -->
</template>

<script setup>
  import { ref } from 'vue'
  import { Switch, SwitchGroup, SwitchLabel } from '@headlessui/vue'
  import { useGlobalStatesStore } from '~/store/globalState'

  const globalSetting = useGlobalStatesStore();
  const { updateLang } = globalSetting;

  // const enabled = ref(false); //false = en - true = fr
  const enabled = computed({
    get() {
      // console.log("in enabled > get :");
      // console.log(globalSetting.displayLang);
      return globalSetting.displayLang;
    },
    set(val) {
      // console.log("in enabled > set :");
      // console.log(val);
      updateLang(val);
    }
  })
</script>

<style scoped>
@media (max-width: 524px) {
  .switch-div {
    color: black;
  }
}
</style>
