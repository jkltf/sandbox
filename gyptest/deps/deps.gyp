{
  'target_defaults': {
    'configurations': {
      'Release': {
        'cflags': ['-Werror'],
        'defines': [
          'NDEBUG'
        ],
        'conditions': [
          ['OS=="win"', {
            'cflags': ['/WX']
          }]
        ]
      },
      'Debug': {
        'defines': [
          'DEBUG'
        ],
        'cflags': ['-Werror'],
        'conditions': [
          ['OS=="win"', {
            'cflags': ['/WX']
          }]
        ]
      }
    }
  },
  'targets': [
    {
      'target_name': 'mongoose',
      'type': 'static_library',
      'defines': [
        'DEBUG'
      ],
      'sources': [
        'mongoose/mongoose.c'
      ],
      'include_dirs': [
        'mongoose'
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'mongoose'
        ]
      }
    }
  ]
}
