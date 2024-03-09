FROM node:13.12.0-alpine as build

WORKDIR /app/front_end

COPY ./front_end/package*.json ./

RUN npm install

COPY ./front_end/ ./

RUN npm run build


FROM nginx:stable-alpine

COPY --from=build /app/front_end/build /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
