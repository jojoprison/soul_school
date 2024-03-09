FROM node:20-alpine AS build

WORKDIR /front_end

COPY ./front_end/package*.json ./
RUN npm install

COPY ./front_end/ ./

RUN npm run build


FROM nginx:stable-alpine

COPY ./web_server/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /front_end/build /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
