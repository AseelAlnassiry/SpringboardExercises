// Same keys and values ES2015
function createInstructor(firstname, lastname) {
  return {
    firstname,
    lastname,
  };
}

// Computed Property Names ES2015
const favoriteNumber = 42;
const instructor = {
  firstname: 'Colt',
  [favoriteNumber]: 'This is my favorite!',
};

// Object Methods ES2015
const inst = {
  firstName: 'Colt',
  sayHi() {
    return 'Hi!';
  },
  sayBye() {
    return this.firstName + ' says bye!';
  },
};

// createAnimal function
function createAnimal(species, verb, noise) {
  return {
    species,
    [verb]() {
      return noise;
    },
  };
}
