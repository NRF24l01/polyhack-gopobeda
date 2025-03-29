export const favoritesMixin = {
  data() {
    return { favorites: [] };
  },
  created() {
    const favorites = localStorage.getItem('favoriteEvents');
    if (favorites) {
      this.favorites = JSON.parse(favorites);
    }
  },
  methods: {
    toggleFavorite(event) {
      const index = this.favorites.findIndex(e => e.id === event.id);
      if (index === -1) {
        this.favorites.push(event);
      } else {
        this.favorites.splice(index, 1);
      }
      localStorage.setItem('favoriteEvents', JSON.stringify(this.favorites));
    },
    isFavorite(eventId) {
      return this.favorites.some(event => event.id === eventId);
    }
  }
}
