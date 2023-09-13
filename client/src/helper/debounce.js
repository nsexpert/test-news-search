
export default {
    mounted(el, binding) {
    let timeout;
    const delay = parseInt(binding.arg) || 700;

    el.addEventListener('input', () => {
      clearTimeout(timeout);
      timeout = setTimeout(() => {
        binding.value();
      }, delay);
    });
  },
  unmounted(el) {
    el.removeEventListener('input');
  },
};