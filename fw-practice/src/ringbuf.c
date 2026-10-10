#include "ringbuf.h"

void ringbuf_init(ringbuf_t *rb)
{
    rb->head = 0u;
    rb->count = 0u;
}

bool ringbuf_put(ringbuf_t *rb, uint8_t value)
{
    if (rb->count >= RINGBUF_SIZE) {
        return false;
    }
    rb->data[(uint8_t)((rb->head + rb->count) % RINGBUF_SIZE)] = value;
    rb->count++;
    return true;
}

bool ringbuf_get(ringbuf_t *rb, uint8_t *value)
{
    if (rb->count == 0u) {
        return false;
    }
    *value = rb->data[rb->head];
    rb->head = (uint8_t)((rb->head + 1u) % RINGBUF_SIZE);
    rb->count--;
    return true;
}
