let genres = [];

fetch("genres.json")
    .then(response => response.json())
    .then(data => {
        genres = data;
        displayGenres();
    })
    .catch(error => {
        console.error('Error loading genres:', error);
    });

function displayGenres() {
    const genresList = document.getElementById('genres-list');
    genres.forEach(genre => {
        const genreButton = document.createElement('button');
        genreButton.innerText = genre.name; 
        genreButton.classList.add('button', 'is-primary', 'm-2'); 
        genreButton.onclick = () => openGenreUrl(genre.url); 
        genresList.appendChild(genreButton); 
    });
}

// Функція для відкриття URL жанру
function openGenreUrl(url) {
    const playerDiv = document.getElementById('player');
    playerDiv.innerHTML = `<iframe src="${url}" width="100%" height="1000" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>`;
    
    const genresList = document.getElementById('genres-list');
    genresList.scrollIntoView({ behavior: 'smooth' });
}
