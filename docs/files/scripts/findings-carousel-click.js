
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".findings-carousel").forEach(carousel => {
      const track = carousel.querySelector(".findings-grid");
      const viewport = carousel.querySelector(".findings-viewport");
      const cards = Array.from(track.querySelectorAll(".finding-card"));
      const prev = carousel.querySelector(".findings-prev");
      const next = carousel.querySelector(".findings-next");
  
      if (!cards.length) return;
  
      let index = 0;
  
      function visibleCount() {
        return parseInt(
          getComputedStyle(carousel).getPropertyValue("--visible-cards"),
          10
        ) || 3;
      }
  
      function updateCarousel() {
        const visible = Math.min(visibleCount(), cards.length);
        const maxIndex = Math.max(0, cards.length - visible);
  
        index = Math.max(0, Math.min(index, maxIndex));
  
        const gap = parseFloat(getComputedStyle(track).columnGap) || 0;
        const cardWidth = cards[0].getBoundingClientRect().width;
  
        track.style.transform =
          `translateX(-${index * (cardWidth + gap)}px)`;
  
        const hasOverflow = cards.length > visible;
        prev.hidden = !hasOverflow;
        next.hidden = !hasOverflow;
      }
  
      next.addEventListener("click", () => {
        const maxIndex = Math.max(0, cards.length - visibleCount());
        index = index >= maxIndex ? 0 : index + 1;
        updateCarousel();
      });
  
      prev.addEventListener("click", () => {
        const maxIndex = Math.max(0, cards.length - visibleCount());
        index = index <= 0 ? maxIndex : index - 1;
        updateCarousel();
      });
  
      window.addEventListener("resize", updateCarousel);
      updateCarousel();
    });
  });
  