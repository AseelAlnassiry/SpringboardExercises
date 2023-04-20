console.log("Let's get this party started!");

const adder = $('#adder');
const remover = $('#remover');
const search = $('input');
const ul = $('ul');

const handleAdd = async (e) => {
  e.preventDefault();
  try {
    const searchTerm = search.val();
    const res = await axios.get('https://api.giphy.com/v1/gifs/search', {
      params: { q: searchTerm, api_key: 'MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym' },
    });
    const url = res.data.data[0].images.original.url;
    addGif(url);
  } catch (err) {
    alert('hey that term is weird bro');
    search.val('');
  }
};

const addGif = (url) => {
  const newLi = $('<li>');
  const newImg = $('<img>');
  newImg.attr('src', url);
  newLi.append(newImg);
  ul.append(newLi);
  search.val('');
};

adder.on('click', handleAdd);
remover.on('click', () => ul.empty());
