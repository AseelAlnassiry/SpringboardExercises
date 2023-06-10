// Identifiers
addForm = $("#add-form");
cupcakeList = $("#all-cupcakes");

const cupcakeMarkup = (cupcake) => {
  newLi = $("<li>");
  newImg = $("<img>");
  topDiv = $("<div>");
  bottomDiv = $("<div>");
  nameSpan = $("<span>");
  ratingSpan = $("<span>");

  newLi.addClass("border bg-pink-300 px-6 py-4 rounded-md");

  bottomDiv.addClass(
    "flex flex-col items-center justiy-center gap-2 pt-2 mt-2 bg-fuchsia-200 rounded-md shadow-lg"
  );

  newImg.attr("src", cupcake.image);
  newImg.addClass("rounded-md h-80 w-60 shadow-lg");

  nameSpan.text(cupcake.flavor.toUpperCase());
  nameSpan.addClass(
    "text-xl bg-indigo-200 rounded-md p-2 text-red-900 font-semibold"
  );

  ratingSpan.text(cupcake.rating);
  ratingSpan.addClass("px-2 py-1 mb-1 bg-amber-200 rounded-md");

  topDiv.append(newImg);

  bottomDiv.append(nameSpan, ratingSpan);
  newLi.append(topDiv, bottomDiv);

  cupcakeList.append(newLi);
};

const handleSubmit = async (e) => {
  e.preventDefault();
  let data = addForm.serializeArray().reduce(function (obj, item) {
    obj[item.name] = item.value;
    return obj;
  }, {});
  await axios.post("/api/cupcakes", data);
  startupProcedure();
};

const startupProcedure = async () => {
  // Get all the cupcakes through axios
  const res = await axios.get("/api/cupcakes");
  const data = res.data.cupcakes;
  // Remove all data inside list
  cupcakeList.empty();
  // Create markup for each cupcake
  for (let cupcake of data) {
    cupcakeMarkup(cupcake);
  }
  // Add event listener for the form
  addForm.submit(handleSubmit);
};

startupProcedure();
