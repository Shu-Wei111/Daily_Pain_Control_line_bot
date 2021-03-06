from linebot.models import TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageAction, ConfirmTemplate, \
    PostbackAction, ButtonsTemplate, URIAction

page_1 = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://tarotapp.s3.amazonaws.com/p/img_pool/BMHtjy_screen-shot-2019-07-22-at-1-38-16-pm-1563817187.png',
                title='【第 1 講】',
                text='簡介',
                actions=[
                    MessageAction(
                        label='進入課程',
                        text='進入課程2_1'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://tarotapp.s3.amazonaws.com/p/img_pool/BMHtjy_screen-shot-2019-07-22-at-1-38-16-pm-1563817187.png',
                title='【第 2 講】',
                text='功能性解剖',
                actions=[
                    MessageAction(
                        label='進入課程',
                        text='進入課程2_2'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://tarotapp.s3.amazonaws.com/p/img_pool/BMHtjy_screen-shot-2019-07-22-at-1-38-16-pm-1563817187.png',
                title='【第 3 講】',
                text='建立疼痛自覺系統',
                actions=[
                    MessageAction(
                        label='進入課程',
                        text='進入課程2_3'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://tarotapp.s3.amazonaws.com/p/img_pool/BMHtjy_screen-shot-2019-07-22-at-1-38-16-pm-1563817187.png',
                title='【第 4 講】',
                text='自我治療簡介',
                actions=[
                    MessageAction(
                        label='進入課程',
                        text='進入課程2_4'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://tarotapp.s3.amazonaws.com/p/img_pool/BMHtjy_screen-shot-2019-07-22-at-1-38-16-pm-1563817187.png',
                title='【第 5 講】',
                text='基本治療',
                actions=[
                    MessageAction(
                        label='進入課程',
                        text='進入課程2_5'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://tarotapp.s3.amazonaws.com/p/img_pool/BMHtjy_screen-shot-2019-07-22-at-1-38-16-pm-1563817187.png',
                title='【第 6 講】',
                text='進階治療',
                actions=[
                    MessageAction(
                        label='進入課程',
                        text='進入課程2_6'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://tarotapp.s3.amazonaws.com/p/img_pool/BMHtjy_screen-shot-2019-07-22-at-1-38-16-pm-1563817187.png',
                title='第 7 講】',
                text='低頭族與電腦族的煩惱',
                actions=[
                    MessageAction(
                        label='進入課程',
                        text='進入課程2_7'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://tarotapp.s3.amazonaws.com/p/img_pool/BMHtjy_screen-shot-2019-07-22-at-1-38-16-pm-1563817187.png',
                title='【第 8 講】',
                text='游泳與投擲運動以及重覆抬舉之隱憂',
                actions=[
                    MessageAction(
                        label='進入課程',
                        text='進入課程2_8'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://tarotapp.s3.amazonaws.com/p/img_pool/BMHtjy_screen-shot-2019-07-22-at-1-38-16-pm-1563817187.png',
                title='【第 9 講】',
                text='告別工傷假',
                actions=[
                    MessageAction(
                        label='進入課程',
                        text='進入課程2_9'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://tarotapp.s3.amazonaws.com/p/img_pool/BMHtjy_screen-shot-2019-07-22-at-1-38-16-pm-1563817187.png',
                title='【第 10 講】',
                text='長輩的救星',
                actions=[
                    MessageAction(
                        label='進入課程',
                        text='進入課程2_10'
                    )
                ]
            )
        ]
    )
)

page_2_1 = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://pic53.photophoto.cn/20191121/0020033028846064_b.jpg',
                title='1-1',
                text='認識疼痛',
                actions=[
                    URIAction(
                        label='影片連結',
                        uri='https://scdc.sharecourse.net:443/video_data'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://pic53.photophoto.cn/20191121/0020033028846064_b.jpg',
                title='1-2',
                text='止痛機制',
                actions=[
                    URIAction(
                        label='影片連結',
                        uri='https://scdc.sharecourse.net:443/video_data'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://pic53.photophoto.cn/20191121/0020033028846064_b.jpg',
                title='1-3',
                text='疼痛發展史',
                actions=[
                    URIAction(
                        label='影片連結',
                        uri='https://scdc.sharecourse.net:443/video_data'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://pic53.photophoto.cn/20191121/0020033028846064_b.jpg',
                title='1-4',
                text='疼痛肌痙孿惡性循環',
                actions=[
                    URIAction(
                        label='影片連結',
                        uri='https://scdc.sharecourse.net:443/video_data'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://pic53.photophoto.cn/20191121/0020033028846064_b.jpg',
                title='1-5',
                text='疼痛痙攣惡行循環與止痛機制',
                actions=[
                    URIAction(
                        label='影片連結',
                        uri='https://scdc.sharecourse.net:443/video_data'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://pic53.photophoto.cn/20191121/0020033028846064_b.jpg',
                title='1-6',
                text='姿勢與疼痛',
                actions=[
                    URIAction(
                        label='影片連結',
                        uri='https://scdc.sharecourse.net:443/video_data'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://pic53.photophoto.cn/20191121/0020033028846064_b.jpg',
                title='1-7',
                text='不良姿勢與肌肉失衡',
                actions=[
                    URIAction(
                        label='影片連結',
                        uri='https://scdc.sharecourse.net:443/video_data'
                    )
                ]
            ),
        ]
    )
)

self_test = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://pic53.photophoto.cn/20191121/0020033028846064_b.jpg',
                title='症狀評估',
                text='',
                actions=[
                    MessageAction(
                        label='進入檢測',
                        text='症狀評估'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://pic53.photophoto.cn/20191121/0020033028846064_b.jpg',
                title='柔軟度檢測',
                text='',
                actions=[
                    MessageAction(
                        label='進入檢測',
                        text='柔軟度檢測'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://pic53.photophoto.cn/20191121/0020033028846064_b.jpg',
                title='潛藏性肌無力',
                text='',
                actions=[
                    MessageAction(
                        label='進入檢測',
                        text='潛藏性肌無力'
                    )
                ]
            )
        ]
    )
)

symptom_evaluation = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://static.wixstatic.com/media/a882dc_44d06a81fc7a4a12a05e3976630bbd55~mv2.jpg/v1/fill/w_320,h_198,al_c,lg_1,q_80/a882dc_44d06a81fc7a4a12a05e3976630bbd55~mv2.webp',
                title='上斜方肌',
                text='頸部',
                actions=[
                    URIAction(
                        label='疼痛症狀',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-9'
                    ),
                    URIAction(
                        label='改善方式',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-5'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://static.wixstatic.com/media/a882dc_de4d45481d5b40eeb880e18b827b98ab~mv2.jpg/v1/fill/w_203,h_270,al_c,lg_1,q_80/a882dc_de4d45481d5b40eeb880e18b827b98ab~mv2.webp',
                title='肩胛提肌',
                text='背部',
                actions=[
                    URIAction(
                        label='疼痛症狀',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-10'
                    ),
                    URIAction(
                        label='改善方式',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-6'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://static.wixstatic.com/media/a882dc_8ace8437532d43af8803969ff299df2a~mv2.jpg/v1/fill/w_355,h_317,al_c,lg_1,q_80/a882dc_8ace8437532d43af8803969ff299df2a~mv2.webp',
                title='下斜方肌',
                text='背部',
                actions=[
                    URIAction(
                        label='疼痛症狀',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-13'
                    ),
                    URIAction(
                        label='改善方式',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-13'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://static.wixstatic.com/media/a882dc_5583d9cb64c743408f2943c2aaa37a3c~mv2.jpg/v1/fill/w_372,h_282,al_c,q_80/a882dc_5583d9cb64c743408f2943c2aaa37a3c~mv2.webp',
                title='胸大肌、胸小肌',
                text='胸',
                actions=[
                    URIAction(
                        label='疼痛症狀',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-12'
                    ),
                    URIAction(
                        label='疼痛改善',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-2'
                    ),
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://static.wixstatic.com/media/a882dc_b8597c23ea1948978bc1a2bca024d9d6~mv2.jpg/v1/fill/w_535,h_302,al_c,q_80/a882dc_b8597c23ea1948978bc1a2bca024d9d6~mv2.webp',
                title='豎脊肌、髂腰肌',
                text='腰',
                actions=[
                    URIAction(
                        label='疼痛症狀',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-14'
                    ),
                    URIAction(
                        label='疼痛改善',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-2'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://static.wixstatic.com/media/a882dc_8baecae1f4894bb2ab681a19eac30cdc~mv2.jpg/v1/fill/w_457,h_234,al_c,q_80,usm_0.66_1.00_0.01/a882dc_8baecae1f4894bb2ab681a19eac30cdc~mv2.webp',
                title='梨狀肌',
                text='臀部',
                actions=[
                    URIAction(
                        label='疼痛症狀',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-15'
                    ),
                    URIAction(
                        label='改善方式',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-40'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://static.wixstatic.com/media/a882dc_35238bd0c965453da03fc94f4c13cb54~mv2.jpg/v1/fill/w_205,h_304,al_c,q_80/a882dc_35238bd0c965453da03fc94f4c13cb54~mv2.webp',
                title='髂脛束',
                text='腿',
                actions=[
                    URIAction(
                        label='疼痛症狀',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-16'
                    ),
                    URIAction(
                        label='改善方式',
                        uri='https://hsianhan95.wixsite.com/e44021123dailypain/blank-39'
                    )
                ]
            )
        ]
    )
)

