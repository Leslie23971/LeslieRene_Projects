<template>
  <div class="main-content flex flex-col gap-y-16">    
    <div class="intro-block grid gap-y-12 grid-cols-4 grid-rows-4 text-2xl font-serif italic">
      <div class="content-1">MY NAME IS <span class="bold-words not-italic font-bold">LESLIE RENE</span>&nbsp;.</div>
      <div class="content-2">I AM A <span class="bold-words not-italic font-bold">SOFTWARE DEVELOPPER</span>&nbsp;,</div>
      <div class="content-3">A TRAVELER ON MY SPARE TIME,</div>
      <div class="content-4 content-4-en">AND AN ARTIST AT HEART.</div>
    </div>
    <div class="resume-downloader">
      <a href="/Rene_Leslie_Resume.pdf" download="" class="resume-downloader-lnk flex flex-row">
        <button class="resume-dwnld-btn">RESUME</button>
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
}
</style>