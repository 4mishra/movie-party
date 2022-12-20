import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const moviesApi = createApi({
    reducerPath: 'movies',
    baseQuery: fetchBaseQuery({ baseUrl: `${process.env.REACT_APP_MOVIES}/api`}),
    endpoints: builder => ({
      getPopular: builder.query({
        query: () => "/movies/popular/",
      }),
    //   getPopular: builder.query({
    //     query: (id) => `movies/${id}`,
    //   }),
    }),
  })

  export const { useGetPopularQuery } = moviesApi;
