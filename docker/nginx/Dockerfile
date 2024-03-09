FROM node:13.12.0-alpine as build

WORKDIR /app/front_end

COPY ./front_end/package.json ./
COPY ./front_end/package-lock.json ./

#RUN npm ci --silent
COPY ./front_end/ ./
RUN npm run build

# The second stage
# Copy React static files and start nginx
FROM nginx:stable-alpine
COPY --from=build /app/front_end/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
