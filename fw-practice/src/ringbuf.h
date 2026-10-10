#ifndef RINGBUF_H
#define RINGBUF_H
#include <stdint.h>
#include <stdbool.h>

#define RINGBUF_SIZE 8u

typedef struct {
    uint8_t data[RINGBUF_SIZE];
    uint8_t head;
    uint8_t count;
} ringbuf_t;

void ringbuf_init(ringbuf_t *rb);
bool ringbuf_put(ringbuf_t *rb, uint8_t value);
bool ringbuf_get(ringbuf_t *rb, uint8_t *value);

#endif
