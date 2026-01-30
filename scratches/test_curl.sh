#!/bin/bash

curl -X POST https://onesignal.com/api/v1/notifications \
  -H "Content-Type: application/json; charset=utf-8" \
  -H "Authorization: Basic os_v2_app_laykg4h2bvhy3mgsjbfmfxl22dpjke3nfbgeyo5ucge7swp6zhftqnnoblg4ilbne6xqymebax7wtytliu2q2ghktjprgyorbiojgua" \
  -d '{
    "app_id": "5830a370-fa0d-4f8d-b0d2-484ac2dd7ad0",
    "include_external_user_ids": ["5293e42a-45c8-4741-9af8-999fbedd6222"],
    "contents": {
      "en": "Test notification"
    }
  }'