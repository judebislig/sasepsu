class Footer extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
    <footer>
      <br>
      <div>
        <a href="https://instagram.com/sasepsu?igshid=MzRlODBiNWFlZA==">
          <iconify-icon icon="mdi:instagram"></iconify-icon></i></a>
        <a href="https://www.linkedin.com/in/sase-penn-state-96b63b26a/"
          ><iconify-icon icon="mdi:linkedin"></iconify-icon></i></a> 
        <a href="https://linktr.ee/sasepsu"
          ><iconify-icon icon="simple-icons:linktree"></iconify-icon></a>
        <a href="https://groupme.com/join_group/85350467/HLs2EFF0"
          ><iconify-icon icon="simple-icons:groupme"></iconify-icon></i></a>
      </div>
      <a href="index.html"><img src="images/sase-logo.png" alt=""> </a> 
      <br><br>
      <p>Society of Asian Scientists and Engineers © 2023 </iconify-icon></p>
      
    </footer>
      `;
  }
}

customElements.define("footer-sase", Footer);
