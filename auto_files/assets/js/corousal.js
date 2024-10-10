jQuery(document).ready(function () {
  const carousel = jQuery(".carousel");
  const slides = jQuery(".carousel-slide");
  const dotsContainer = jQuery(".carousel-dots");
  let currentIndex = 0;
  let autoplayInterval;

  // Create dots
  slides.each((index) => {
    dotsContainer.append(
      `<div class="dot${index === 0 ? " active" : ""}"></div>`
    );
  });

  // Update carousel position
  function updateCarousel() {
    carousel.css("transform", `translateX(-${currentIndex * 100}%)`);
    jQuery(".dot").removeClass("active").eq(currentIndex).addClass("active");
  }

  // Next slide
  function nextSlide() {
    resetAutoplay();
    currentIndex = (currentIndex + 1) % slides.length;
    updateCarousel();
  }

  // Previous slide
  function prevSlide() {
    resetAutoplay();
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateCarousel();
  }

  // Click events
  jQuery(".next").click(nextSlide);
  jQuery(".prev").click(prevSlide);

  // Dot navigation
  jQuery(".dot").click(function () {
    currentIndex = jQuery(this).index();
    updateCarousel();
    resetAutoplay();
  });

  // Autoplay
  function startAutoplay() {
    autoplayInterval = setInterval(nextSlide, 5000);
  }

  function resetAutoplay() {
    clearInterval(autoplayInterval);
    startAutoplay();
  }

  // Touch/swipe functionality
  let touchStartX = 0;
  let touchEndX = 0;

  carousel.on("touchstart", function (e) {
    touchStartX = e.touches[0].clientX;
  });

  carousel.on("touchend", function (e) {
    touchEndX = e.changedTouches[0].clientX;
    handleSwipe();
  });

  function handleSwipe() {
    const swipeThreshold = 50;
    const difference = touchStartX - touchEndX;

    if (Math.abs(difference) > swipeThreshold) {
      if (difference > 0) {
        nextSlide();
      } else {
        prevSlide();
      }
      resetAutoplay();
    }
  }

  // Start autoplay
  startAutoplay();
});
