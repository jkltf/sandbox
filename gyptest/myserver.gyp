{
  'target_defaults': {
    'configurations': {
      'Release': {
        'cflags': ['-Werror'],
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
      'target_name': 'myserver',
      'type': 'executable',
      'include_dirs': [
        'src'
      ],
      'sources': [
        'src/main.c'
      ],
      'dependencies': [
        'libmyserver'
      ]
    },
    {
      'target_name': 'libmyserver',
      'type': 'static_library',
      'include_dirs': [
        'src'
      ],
      'sources': [
        'src/myserver.c'
      ],
      'dependencies': [
        'deps/deps.gyp:mongoose'
      ]
    }
  ]
}
