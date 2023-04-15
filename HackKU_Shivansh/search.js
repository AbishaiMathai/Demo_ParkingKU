const searchInput = document.getElementById('search-input');
const searchResults = document.getElementById('search-results');

// Fetch data from server (replace with your own data source)
function fetchData() {
  return new Promise((resolve) => {
    // Replace with your own data source URL
    fetch('https://example.com/api/parking-lots')
      .then((response) => response.json())
      .then((data) => resolve(data));
  });
}

// Filter data by keyword
function filterData(keyword, data) {
  return data.filter((item) => item.name.toLowerCase().includes(keyword.toLowerCase()));
}

// Show search results
function showResults(results) {
  searchResults.innerHTML = '';
  results.forEach((result) => {
    const resultItem = document.createElement('div');
    resultItem.className = 'search-result';
    resultItem.textContent = result.name;
    searchResults.appendChild(resultItem);
    resultItem.addEventListener('click', () => {
      searchInput.value = result.name;
      searchResults.style.display = 'none';
    });
  });
  searchResults.style.display = 'block';
}

// Handle search input
searchInput.addEventListener('input', async () => {
  const keyword = searchInput.value.trim();
  if (keyword.length < 2) {
    searchResults.style.display = 'none';
    return;
  }
  const data = await fetchData();
  const filteredData = filterData(keyword, data);
  showResults(filteredData);
});