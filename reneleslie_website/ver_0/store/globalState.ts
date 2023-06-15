import { defineStore } from 'pinia'

export const useGlobalStatesStore = defineStore({
  id: 'websiteglobalsettings',
  state: () => ({
    displaylang: false,
  }),
  actions: {
    updateLang(value: boolean) {
    //   console.log("in updateLang :");
    //   console.log(value);
      this.displaylang = value
    },
  },
  getters: {
    displayLang: state => state.displaylang,
  },
})