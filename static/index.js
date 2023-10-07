// Get the animated text element
const animatedText = document.getElementById('animatedText');

// List of words to display
const wordList = ['PYTHON PROGRAMMER', 'SOFTWARE DEVELOPER', 'WEB SCRABBER','SIMPLE APP DEVELOPER','C AND PYTHON CODER', 'AI DEVELOPER AND TRAINNER','DATA SCIENTIST AND MANIPUlATER', 'SIMPLE WEB DEVELOPER'];
// Function to change the text and trigger animations
function changeText() {
    animatedText.classList.remove('appear'); // Remove the 'appear' class
    animatedText.classList.add('disappear'); // Add the 'disappear' class

    // Wait for the animation to complete and then change the text
    setTimeout(() => {
        // Get the next word in the list
        const currentWord = animatedText.textContent;
        const currentIndex = wordList.indexOf(currentWord);
        const nextIndex = (currentIndex + 1) % wordList.length;
        const nextWord = wordList[nextIndex];

        animatedText.textContent = nextWord;
        animatedText.classList.remove('disappear'); // Remove the 'disappear' class
        animatedText.classList.add('appear'); // Add the 'appear' class

        // Call the function again with a delay
        setTimeout(changeText, 5000); // Delay of 5 seconds (5000 milliseconds)
    }, 500); // Adjust the time to match your animation duration
}

// Start the animation automatically when the page loads
window.onload = function() {
    changeText();
};

// Custom JavaScript to expand the text area
document.addEventListener("input", function (e) {
    if (e.target && e.target.nodeName === "TEXTAREA") {
        autoExpand(e.target);
    }
});

function autoExpand(textarea) {
    textarea.style.height = "auto";
    textarea.style.height = (textarea.scrollHeight) + "px";
}

document.addEventListener("DOMContentLoaded", function () {
    const textContainers = document.querySelectorAll(".text-container");

    textContainers.forEach(function (textContainer) {
        const truncateText = textContainer.querySelector(".truncate-text");
        const readMoreBtn = textContainer.querySelector(".read-more");
        const readLessBtn = textContainer.querySelector(".read-less");

        readMoreBtn.addEventListener("click", function (e) {
            e.preventDefault();
            truncateText.style.whiteSpace = "normal";
            readMoreBtn.style.display = "none";
            readLessBtn.style.display = "inline";
        });

        readLessBtn.addEventListener("click", function (e) {
            e.preventDefault();
            truncateText.style.whiteSpace = "nowrap";
            readMoreBtn.style.display = "inline";
            readLessBtn.style.display = "none";
        });
    });
});


// Select the element by its class
const element = document.querySelector('.anim');
// Store the original color
// const originalColor = getComputedStyle(element).backgroundColor;
// Add a scroll event listener to track the element's position
window.addEventListener('scroll', () => {
  // Calculate the element's position from the top
  const elementTop = element.getBoundingClientRect().top;

  // Check if the position is greater than 5 pixels from the top
  if (elementTop == 0) {
    // Change the color when it's greater than 5 pixels from the top
    element.style.color = "green";
    element.style.backgroundColor = "#B1C0CB";
  } else{
    // Revert the color when it's less than 5 pixels from the top
    element.style.color = "white";
    element.style.backgroundColor = "";
  }
});

