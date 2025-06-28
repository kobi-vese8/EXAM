from rest_framework import serializers
from .models import Manager, StaffBase, Intern


class StaffBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '_all_'


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '_all_'


class InternSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    resume = ResumeSerializer()

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'dob',
            'email',
            'phone_number',
            'address',
            'resume',
        ]

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        resume_data = validated_data.pop('resume')

        address = Address.objects.create(**address_data)
        resume = Resume.objects.create(**resume_data)

        user = CustomUser.objects.create(address=address, resume=resume, **validated_data)
        return user

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        resume_data = validated_data.pop('resume', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if address_data:
            for attr, value in address_data.items():
                setattr(instance.address, attr, value)
            instance.address.save()

        if resume_data:
            for attr, value in resume_data.items():
                setattr(instance.resume, attr, value)
            instance.resume.save()

        return instance


class CompanyProfileSerializer(serializers.ModelSerializer):
    company_address = AddressSerializer()

    class Meta:
        model = CompanyProfile
        fields = '_all_'

    def create(self, validated_data):
        address_data = validated_data.pop('company_address')
        address = Address.objects.create(**address_data)
        company = CompanyProfile.objects.create(company_address=address, **validated_data)
        return company

    def update(self, instance, validated_data):
        address_data = validated_data.pop('company_address', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if address_data:
            for attr, value in address_data.items():
                setattr(instance.company_address, attr, value)
            instance.company_address.save()

        return instance