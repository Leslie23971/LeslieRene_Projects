<template>
  <div class="main-content flex flex-col gap-y-16">    
    <div class="intro-block grid gap-y-12 grid-cols-4 grid-rows-4 text-2xl font-serif italic">
      <div class="content-1">JE ME PRÉNOMME <span class="bold-words not-italic font-bold">LESLIE RENE</span>&nbsp;,</div>
      <div class="content-2 content-2-fr"><span class="bold-words not-italic font-bold">INGÉNIEURE DEVELLOPEMENT LOGICIEL</span>&nbsp;,</div>
      <div class="content-3 content-3-fr">VOYAGEUSE À MES HEURES PERDUES,</div>
      <div class="content-4 content-4-fr">ET ARTISTE DE COEUR.</div>
    </div>
    <div class="resume-downloader">
      <a href="/Rene_Leslie_Resume.pdf" download="" class="resume-downloader-lnk flex flex-row">
        <button class="resume-dwnld-btn">CV</button>
      </a>      
    </div>
  </div>
</template>
    
<script setup></script>
  
<style scoped>
@media (max-width: 375px) {
  .resume-dwnld-btn {
    font-size: x-small;
    height: 16px;
    width: 25%;
    padding-top: 0.7rem;
    padding-bottom: 1.4rem;
  }
  .content-2-fr .bold-words {
    font-size: x-small;
    font-weight: bold;
  }
}
</style>