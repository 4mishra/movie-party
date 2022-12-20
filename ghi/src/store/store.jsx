import { configureStore } from '@reduxjs/toolkit';
import { moviesApi } from './moviesApi';
import { setupListeners } from '@reduxjs/toolkit/query/react';


export const store = configureStore({
    reducer: {
      [moviesApi.reducerPath]: moviesApi.reducer,
    },
    middleware: getDefaultMiddleware =>
      getDefaultMiddleware().concat(moviesApi.middleware),
  })

  setupListeners(store.dispatch);
