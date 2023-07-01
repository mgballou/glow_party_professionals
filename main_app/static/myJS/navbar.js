function extractPath(url) {
    const urlObj = new URL(url);
    const pathSegments = urlObj.pathname.split('/');
    const firstSegment = pathSegments[1] || '';
    return firstSegment;
}

let currentPage = extractPath(window.location.href)
console.log(currentPage)

if (currentPage === ""){
    currentPage = "home"
}

const currentPageLink = document.querySelector(`#${currentPage}`)

currentPageLink.classList.add("active")


